class EvidenceCaptureService:

    async def execute(self, url: str):
        captured_page = await self.page_capture.capture(url)

        hash = self.hash_service.generate(
            captured_page.html
        )

        evidence = await self.evidence_create_service.execute(
            ...
        )

        snapshot = EvidenceSnapshot.create(
            evidence=evidence,
            html_path=captured_page.html_path,
            screenshot_path=captured_page.screenshot_path,
            hash=hash
        )

        await self.snapshot_repository.create(snapshot)

        return evidence
